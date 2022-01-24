
# Key: a336a4eba98dea134be766978db81b4d
# Secret: 2f84fa08520c65f019ff20b1f7bf0b1a8bb8447db4c33d7ed97ec22a00fd7bff
# !/usr/bin/env python
# coding: utf-8
import logging
from argparse import ArgumentParser

from config import RunConfig
from spot import spot_demo

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser(description="Run Gate APIv4 demo application")
    parser.add_argument("-k", "--key", required=False, help="Gate APIv4 Key") # was required=True
    parser.add_argument("-s", "--secret", required=False, help="Gate APIv4 Secret") # was required=True
    parser.add_argument("-u", "--url", required=False, help="API base URL used to test")
    options = parser.parse_args()

    host_used = options.url
    if not host_used:
        host_used = "https://api.gateio.ws/api/v4"
    if not host_used.startswith("http"):
        host_used = "https://" + host_used
    host_used = host_used.rstrip("/")
    if not host_used.endswith("/api/v4"):
        host_used += '/api/v4'

    # run_config = RunConfig(options.key, options.secret, host_used)
    run_config = RunConfig("a336a4eba98dea134be766978db81b4d",
                    "2f84fa08520c65f019ff20b1f7bf0b1a8bb8447db4c33d7ed97ec22a00fd7bff", host_used)
    spot_demo(run_config)

if __name__ == '__main__':
    main()
