import logging
import control_tools

log = logging.getLogger(__name__)


def main():
    log.info(f"application version {control_tools.__version__} start")


if __name__ == "__main__":
    main()