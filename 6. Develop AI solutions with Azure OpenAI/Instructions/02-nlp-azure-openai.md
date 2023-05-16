---
lab:
    title: 'Develop NLP solutions with Azure Ope AI'
---
# Develop NLP solutions with Azure OpenAI

Azure OpenAI provides a platform for developers to add artificial intelligence functionality to their applications with the help of both Python and C# SDKs and REST APIs. In this exercise, you'll learn how to deploy a model in Azure OpenAI and use it in your own application.

## Before you start

You will need an Azure subscription that has been approved for access to the Azure OpenAI service.

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
4. Navigate to **Keys and Endpoint** page, and save those to a text file to use later.

## Deploy a model

Azure OpenAI provides a web-based portal named **Azure OpenAI Studio**, that you can use to deploy, manage, and explore models. You'll start your exploration of Azure OpenAI by using Azure OpenAI Studio to deploy a model.

1. On the **Overview** page for your Azure OpenAI resource, use the **Explore** button to open Azure OpenAI Studio in a new browser tab.
2. In Azure OpenAI Studio, create a new deployment with the following settings:
    - **Model name**: text-davinci-003
    - **Deployment name**: text-davinci

> **Note**: Please ignore this step if you have already deployed this model in the previous exercise.

## Create a new .Net Core application
You can create a new .Net Core console application either using a console window (such as cmd, PowerShell, or Bash) or Visual Studio. 

    **.NET CLI**

    ```bash
    dotnet new console -n generate-text
    ```
    
### Visual Studio:
There are multiple ways to create a new project in Visual Studio. When you first open Visual Studio, the start window appears, and from there, you can select Create a new project. If the Visual Studio development environment is already open, you can create a new project by choosing File > New > Project on the menu bar. You can also select the New Project button on the toolbar, or press Ctrl+Shift+N.
Select "Console App" template and type the name of the project as "generate-text".

## Build .Net Core application

### .NET CLI:
dotnet build

### Visual Studio:
On the menu bar, choose Build, and then choose one of the following commands:
Choose Build or Build Solution, or press Ctrl+Shift+B, to compile only those project files and components that have changed since the most recent build.

## Install the OpenAI .NET client library

### .NET CLI:
dotnet add package Azure.AI.OpenAI --prerelease
    
    **C#**

    ```bash
    cd CSharp
    dotnet add package Azure.AI.OpenAI --prerelease
    ```

### Visual Studio:
Install the client library for .NET with NuGet https://www.nuget.org/packages/Azure.AI.OpenAI

## Retrieve Key and endpoint

To successfully make a call against Azure OpenAI, you'll need an endpoint and a key. Go to your resource in the Azure portal. The Endpoint and Keys can be found in the Resource Management section.

## Set the environment vaiables

setx AZURE_OPENAI_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE"
setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_KEY_VALUE_HERE"

## Update the program.cs file

From the project directory, open the program.cs file and replace with the following code:

    **C#**

    ```bash
    using Azure;
    using Azure.AI.OpenAI;
    using static System.Environment;

    string endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
    string key = GetEnvironmentVariable("AZURE_OPENAI_KEY");

    // Enter the deployment name you chose when you deployed the model.
    string engine = "text-davinci";

    OpenAIClient client = new(new Uri(endpoint), new AzureKeyCredential(key));

    string prompt = "What is the name of the capital of India??";
    Console.Write($"Prompt : {prompt}\n");

    Response<Completions> completionsResponse = 
        await client.GetCompletionsAsync(engine, prompt);
    string completion = completionsResponse.Value.Choices[0].Text;
    Console.WriteLine($"Azure OpenAI response: {completion}");
    ```

## Run the application

### .NET CLI:
dotnet run program.cs

### Visual Studio:
To start building the program, press the green Start button on the Visual Studio toolbar, or press F5 or Ctrl+F5. Using the Start button or F5 runs the program under the debugger.

## Clean up

When you're done with your Azure OpenAI resource, remember to delete the deployment or the entire resource in the [Azure portal](https://portal.azure.com?azure-portal=true).


