from subprocess import Popen, PIPE, STDOUT
import json
from psdvs.consumer import Consumer
from psdvs.avro_serializer import DVSAvroSerializer
from psdvs.config import get_configuration
import shlex
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

fileconfig = get_configuration()


def file_output(filepath=None):
    log.debug("Creating file pipe output")
    filenum = 1

    while True:
        command = "ssh -i /Users/mikepk/.pems/mpk-sandbox.pem hadoop@ec2-54-204-74-217.compute-1.amazonaws.com hdfs dfs -put - exp.prism.PayloadUpdated-2-{}.json".format(filenum)
        # command = "python3 testapp.py"
        # path = "hdfs://{}".format(filepath)
        # command = "hdfs dfs -put - {}".format(path)
        command_list = shlex.split(command)
        # encoding argument makes all the pipes text streams
        with Popen(command_list, stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding="utf-8") as p:
            # stdout_data = p.communicate(input='data_to_write')[0]
            total_records = 0
            try:
                while True:
                    json_record = (yield)
                    total_records += 1
                    if total_records % 5000 == 0:
                        log.debug("output {} records".format(total_records))
                    if total_records > 50000:
                        filenum += 1
                        break
                    # write the record to the stdin of the subprocess
                    p.stdin.write(json_record+"\n")
                    # p.stdin.flush() # the flush fails in streaming over ssh
            except GeneratorExit:
                log.debug("Closing pipe output!")
                break

def make_handler(topic, processor):
    serializer = DVSAvroSerializer(topic=topic,
                                   schema_registry_config=fileconfig["schema_registry"])
    # create a coroutine to process the records
    def handle_message(key, msg, partition, offset):
        record = serializer.deserialize(msg)
        json_record = json.dumps(record)
        pipe_output.send(json_record)
    return handle_message


consumer = Consumer(fileconfig["kafka"], consumer_group="data-eng--sample1")

pipe_output = file_output()
next(pipe_output)

consumer.subscribe("exp.prism.PayloadUpdated",
                   callback=make_handler("exp.prism.PayloadUpdated", pipe_output),
                   offset="beginning")
try:
    consumer.run()
finally:
    pipe_output.close()
    log.info("Shutting down!")