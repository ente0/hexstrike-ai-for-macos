import argparse
import sys
from hexstrike_server import app, BANNER, API_PORT, DEBUG_MODE, ModernVisualEngine, logger, COMMAND_TIMEOUT, CACHE_SIZE, CACHE_TTL
import logging

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Run the HexStrike AI API Server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--port", type=int, default=API_PORT, help=f"Port for the API server (default: {API_PORT})")
    args = parser.parse_args()
    
    _debug = args.debug
    _port = args.port
    if _debug:
        logger.setLevel(logging.DEBUG)
    
    app.run(host="0.0.0.0", port=_port, debug=_debug)

if __name__ == "__main__":
    main()
