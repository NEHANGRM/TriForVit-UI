#!/usr/bin/env python3
"""
server.py - Standalone Static HTTP Server with CORS for ForgeSight UI
Enables running the UI locally or deploying to any Python-compatible container/host.
"""

import sys
import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

def main():
    parser = argparse.ArgumentParser(description="ForgeSight Static Server")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8080)), help="Port to listen on")
    parser.add_argument("--bind", type=str, default="0.0.0.0", help="Address to bind to")
    args = parser.parse_args()

    # Change to the directory of this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    server_address = (args.bind, args.port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f"\n========================================================")
    print(f"  ForgeSight (TriForVit) Web Application Server")
    print(f"  Listening on: http://{args.bind}:{args.port}")
    print(f"========================================================\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    main()
