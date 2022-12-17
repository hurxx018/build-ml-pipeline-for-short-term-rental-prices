# Build an ML Pipeline for Short-Term Rental Prices in NYC
You are working for a property management company renting rooms and properties for short periods of
time on various rental platforms. You need to estimate the typical price for a given property based
on the price of similar properties. Your company receives new data in bulk every week. The model needs
to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

## Instruction
See REAMDME_instruction.md

## Run a mlflow using the pipeline
mlflow run https://github.com/hurxx018/build-ml-pipeline-for-short-term-rental-prices -v 1.0.1 -P hydra_options="etl.sample='sample2.csv'"


## W&B Project
https://wandb.ai/hurxx018/nyc_airbnb