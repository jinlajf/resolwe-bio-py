import resdk

# Create a Resolwe object to interact with the server
res = resdk.Resolwe('<USERNAME>', '<PASSWORD>', 'https://app.genialis.com')

# Print command details to stdout
resdk.start_logging()

# Get sample meta-data from the server
sample = res.sample.get('human-example-chr22')

# Download files associated with the sample
sample.download()
