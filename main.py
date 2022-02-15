import fastapi_basic

import uvicorn


from argparse import ArgumentParser


def parse_arguments() -> ArgumentParser:
    """
    This Function Get Argument and Parse
    :return: Argument Parser
    """
    # Create argument parser
    parser = ArgumentParser()

    # Positional mandatory arguments
    parser.add_argument("-d", "--debug", help="Is Debug Mode", type=bool,
                        default=False)
    parser.add_argument("-r", "--reload", help="Change Reload", type=bool,
                        default=False)
    parser.add_argument("-log", "--access-log", help="Access Log Open or Close",
                        type=bool, default=False)
    parser.add_argument("-env", help="Environment File Path", type=str,
                        default=".env")

    # Parse arguments
    args = parser.parse_args()

    return args


def run(args: ArgumentParser):
    """
    This function run Fast API with Uvicorn
    :param args:
    :return:
    """
    uvicorn.run(
        app="fastapi_basic.router:app",
        host="0.0.0.0",
        port=5555,
        reload=args.reload,
        debug=args.debug,
        access_log=args.access_log,
        env_file=args.env,
    )


if __name__ == "__main__":
    run(args=parse_arguments())
