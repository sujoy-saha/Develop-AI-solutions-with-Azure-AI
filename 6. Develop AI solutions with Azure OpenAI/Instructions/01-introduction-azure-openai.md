---
lab:
    title: 'Introduction to Azure OpenAI Services'
---
# Introduction to Azure OpenAI Services

Azure OpenAI Service helps developers to build powerful AI solutions quickly using Azure cloud platform. In this exercise, you’ll explore how to create an Azure OpenAI service and deploy OpenAI models using Azure OpenAI Studio.

## Before you start

You'll need an Azure subscription that has been approved for access to the Azure OpenAI service.

- To sign up for a free Azure subscription, visit [https://azure.microsoft.com/free](https://azure.microsoft.com/free).
- To request access to the Azure OpenAI service, visit [https://aka.ms/oaiapply](https://aka.ms/oaiapply).

## Provision an Azure OpenAI resource

Before you can use Azure OpenAI models, you must provision an Azure OpenAI resource in your Azure subscription.

1. Sign into the [Azure portal](https://portal.azure.com).
2. Create an **Azure OpenAI** resource with the following settings:
    - **Subscription**: An Azure subscription that has been approved for access to the Azure OpenAI service.
    - **Resource group**: Create a new resource group with a name of your choice.
    - **Region**: Choose any available region.
    - **Name**: A unique name of your choice.
    - **Pricing tier**: Standard S0
3. Wait for deployment to complete. Then go to the deployed Azure OpenAI resource in the Azure portal.

## Deploy a model

Azure OpenAI provides a web-based portal named **Azure OpenAI Studio**, that you can use to deploy, manage, and explore models. You'll start your exploration of Azure OpenAI by using Azure OpenAI Studio to deploy a model.

1. On the **Overview** page for your Azure OpenAI resource, use the **Explore** button to open Azure OpenAI Studio in a new browser tab.
2. In Azure OpenAI Studio, create a new deployment with the following settings:
    - **Model name**: text-davinci-003
    - **Deployment name**: text-davinci

## Explore a model in the Completions playground

*Playgrounds* are useful interfaces in Azure OpenAI Studio that you can use to experiment with your deployed models without needing to develop your own client application.

1. In Azure OpenAI Studio, in the left pane under **Playground**, select **Completions**.
2. In the **Completions** page, ensure your **text-davinci** deployment is selected and then in the **Examples** list, select **Summarize an article (abstractive)**.

    The summarize text sample consists of a *prompt* that provides some text, starting with the line **Provide a summary of the text below...**. Starting the prompt with this sentence tells the model to summarize the following block of text.

3. At the bottom of the page, note the number of *tokens* detected in the text. Tokens are the basic units of a prompt - essentially words or word-parts in the text.
4. Use the **Generate** button to submit the prompt to the model and retrieve a response.

    The response consists of a summary of the original text. The summary should communicate the key points from the original text in less verbose language.

5. Use the **Regenerate** button to resubmit the prompt, and note that the response may vary from the original one. A generative AI model can produce new language each time it's called.
6. Under the summarized response, add a new line and enter the following text:

    *How has AI advanced?*

7. Use the **Generate** button to submit the new prompt and review the response. The previous prompt and response provide context in an ongoing dialog with the model, enabling the model to generate an appropriate answer to your question.
8. Replace the entire contents of the prompt with the following text:

    *Provide a summary of the text below that captures its main idea.* 
    
    *Azure OpenAI Service provides REST API access to OpenAI's powerful language models including the GPT-4, Codex and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or our web-based interface in the Azure OpenAI Studio.*

9. Use the **Generate** button to submit the new prompt and verify that the model summarizes the text appropriately.

## Use a model to classify text

So far, you've seen how to use a model to summarize text. However, the generative models in Azure OpenAI can support a range of different types of task. Let's explore a different example; *text classification*.

1. In the **Completions** page, ensure your **text-davinci** deployment is selected and then in the **Examples** list, select **Classify text**.

    The classify text sample prompt describes the context for the model in the form of an instruction to classify a news article into one of a range of categories. It then provides the text for the news article (prefixed by *News article:*) and ends with *Classified category:*. The intention is that the model "completes" the final line of the prompt by predicting the appropriate category.

2. Use the **Generate** button to submit the prompt to the model and retrieve a response. The model should predict an appropriate category for the news article.
3. Under the predicted category, add the following text:

    *news article: Microsoft releases Azure OpenAI service. Microsoft corporation has released an Azure service that makes OpenAI models available for application developers building apps and services in the Azure cloud.*

    *Classified category:*

4. Use the **Generate** button to continue the dialog with the model and generate an appropriate categorization for the new news article.

## Explore code-generation

The **text-davinci** model you deployed is a good general model that can handle most tasks well. However, in some cases it's better to choose a model that is optimized for a specific kind of task. For example, Azure openAI models can be used to generate computer code rather than natural language text, and some models have been optimized for that task.

1. In Azure OpenAI Studio, view the **Models** page; which lists all of the available models in your Azure OpenAI service resource.
2. Select the **code-davinci-002** model and use the **Deploy model** button to deploy it with the deployment name **code-davinci**.
3. After deployment is complete, in Azure OpenAI Studio, view the **Deployments** page; which lists the models you've deployed.
4. Select the **code-davinci** model deployment and use the **Open in Playground** button to open it in the playground.
5. In the **Completions** page, ensure your **code-davinci** deployment is selected and then in the **Examples** list, select **Natural language to SQL**.

    The natural language to SQL sample prompt provides details of tables in a database, and a description of the query that is required followed by the `SELECT` keyword. The intention is for the model to complete the `SELECT` statement to create a query that satisfies the requirement.

6. Use the **Generate** button to submit the prompt to the model and retrieve a response, which consists of a SQL `SELECT` query.
7. Replace the entire prompt and response with the following new prompt:

    *# Python 3*

    *# Create a function to print "Hello " and a specified string*

    *def print_hello(s):*

8. Use the **Generate** button to submit the prompt and view the code that gets generated. The prompt included an indication of the programming language to be generated (Python 3), a comment describing the desired functionality, and the first part of the function definition. The **code-davinci** model should have completed the function with appropriate Python code.

In this exercise, you've learned how to provision the Azure openAI service in an Azure subscription, and how to use Azure OpenAI Studio to deploy and explore models.

