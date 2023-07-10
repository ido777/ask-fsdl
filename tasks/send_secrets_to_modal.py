import os
import subprocess
from pretty_log import pretty_log
from dotenv import load_dotenv


def modal_secret_create(name, secrets):
    command = ["modal", "secret", "create", name]
    for key, value in secrets.items():
        command.append(f"{key}={value}")
    subprocess.run(command, check=True)


def mongo_secrets(name: str = "mongodb-fsdl"):
    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    modal_secret_create(
        name,
        {
            "MONGODB_USER": MONGODB_USER,
            "MONGODB_HOST": MONGODB_HOST,
            "MONGODB_PASSWORD": MONGODB_PASSWORD,
        },
    )


def openai_secrets(name: str = "openai-api-key-fsdl"):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    modal_secret_create(name, {"OPENAI_API_KEY": OPENAI_API_KEY})


def gantry_secrets(name: str = "gantry-api-key-fsdl"):
    GANTRY_API_KEY = os.getenv("GANTRY_API_KEY")
    if GANTRY_API_KEY == "":
        pretty_log("GANTRY_API_KEY not set. Logging will not be available.")
    modal_secret_create(name, {"GANTRY_API_KEY": GANTRY_API_KEY})


def aws_secrets(name: str = "aws-credentials-fsdl"):
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
    modal_secret_create(
        name,
        {
            "AWS_ACCESS_KEY_ID": AWS_ACCESS_KEY_ID,
            "AWS_SECRET_ACCESS_KEY": AWS_SECRET_ACCESS_KEY,
            "AWS_S3_BUCKET_NAME": AWS_S3_BUCKET_NAME,
        },
    )


def main():
    load_dotenv()

    mongo_secrets()
    openai_secrets()
    gantry_secrets()
    aws_secrets()


if __name__ == "__main__":
    main()
