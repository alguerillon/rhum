import sys
from rhum.rhumlogging import get_logger 
from rhum.rhum import RhumDaemon

_pid_file = '/tmp/daemon-rhum.pid'


if __name__ == "__main__":
    logger = get_logger('RHUM-MAIN')
    logger.debug('rhum service manager : ')
    
    daemon = RhumDaemon(_pid_file)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            logger.info("Starting Rhum")
            daemon.start()
        elif 'stop' == sys.argv[1]:
            logger.info("Stopping Rhum")
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            logger.info("Restarting Rhum")
            daemon.restart()
        elif 'reload' == sys.argv[1]:
            logger.info("Reloading Rhum")
            daemon.reload()
        else:
            logger.error("Unknow command of Rhum service")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: {0} start|stop|restart".format(sys.argv[0]))
        sys.exit(2)