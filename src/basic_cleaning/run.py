#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import os

import pandas as pd

import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    logger.info("Downloading artifact")
    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()

    logger.info("Load data")
    df = pd.read_csv(artifact_path)


    logger.info("Drop outliers")
    min_price = args.min_price
    max_price = args.max_price
    idx = df['price'].between(min_price, max_price)
    df = df[idx].copy()

    logger.info("Convert last_review to datetime")
    df['last_review'] = pd.to_datetime(df['last_review'])

    filename = "clean_data.csv"
    df.to_csv(filename, index=False)

    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(filename)

    logger.info("Logging artifact")
    run.log_artifact(artifact)

    os.remove(filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="basic data cleaning")


    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Name of raw data", ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Name of preprocessed data",
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="Type of preprocessed data",
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="Description of preprocess",
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="Minimum value of price",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="Maximum value of price",
        required=True
    )


    args = parser.parse_args()

    go(args)
