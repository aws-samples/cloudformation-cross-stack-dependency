# Coordinating complex resource dependencies across CloudFormation stacks

This repository shows an examples of how to define granular, de-centralized cross-stack dependencies

It's provided in support of blog post "Coordinating complex resource dependencies across CloudFormation stacks".

## Running example

There are two templates used in this example:
* **dependency.yaml**: defines a network baseline with a VPC and subnet
* **dependent.yaml**: defines a bastion host template, that uses subnet in the other stack

Code uses [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html), and requires [SAM CLI to be installed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) in order to build and deploy them.

Templates are not required to be deployed in any specific order, but stacks that have unfulfilled dependencies will timeout eventually. This example sets the timeout to 3600 seconds (1 hour).

To build and deploy the dependency with the default parameter values:

```
$ sam build -t dependency.yaml && sam deploy --guided
```

And to build and deploy the dependent with the default parameter values:

```
$ sam build -t dependent.yaml && sam deploy --guided
```

Note that SAM CLI watches for CloudFormation progess until stack is fully provisioned before exiting. This means deploying dependent template before its dependency will cause the CLI to look stuck in a WaitCondition. This is by design.

You can use another terminal to deploy the dependency template. It's also safe to exit from the CLI, if you don't want to follow process in the CLI.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
