---
lab:
    title: 'Prompt engineering with Azure OpenAI'
---
# Prompt engineering with Azure OpenAI



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
    - **Model name**: gpt-35-turbo
    - **Deployment name**: text-turbo

## Apply prompt engineering in chat playground

Before using your app, examine how prompt engineering improves the model response in the playground. In this first example, imagine you are trying to write a python app of animals with fun names.

1. In [Azure OpenAI Studio](https://oai.azure.com/?azure-portal=true), navigate to the **Chat** playground in the left pane.
1. In the **Assistant setup** section at the top, enter `You are a helpful AI assistant` as the system message.
1. In the **Chat session** section, enter the following prompt and press *Enter*.

    ```code
    1. Create a list of animals
    2. Create a list of whimsical names for those animals
    3. Combine them randomly into a list of 25 animal and name pairs
    ```

1. The model will likely respond with an answer to satisfy the prompt, split into a numbered list. This is a good response, but not what we're looking for.
1. Next, update the system message to include instructions `You are an AI assistant helping write python code. Complete the app based on provided comments`. Click **Save changes**
1. Format the instructions as python comments. Send the following prompt to the model.

    ```code
    # 1. Create a list of animals
    # 2. Create a list of whimsical names for those animals
    # 3. Combine them randomly into a list of 25 animal and name pairs
    ```

1. The model should correctly respond with complete python code doing what the comments requested.
1. Next we'll see the impact of few shot prompting when attempting to classify articles. Return to the system message, and enter `You are a helpful AI assistant` again, and save your changes. This will create a new chat session.
1. Send the following prompt to the model.

    ```code
    Severe drought likely in California

    Millions of California residents are bracing for less water and dry lawns as drought threatens to leave a large swath of the region with a growing water shortage.
    
    In a remarkable indication of drought severity, officials in Southern California have declared a first-of-its-kind action limiting outdoor water use to one day a week for nearly 8 million residents.
    
    Much remains to be determined about how daily life will change as people adjust to a drier normal. But officials are warning the situation is dire and could lead to even more severe limits later in the year.
    ```

1. The response will likely be some information about drought in California. While not a bad response, it's not the classification we're looking for.
1. In the **Assistant setup** section near the system message, select the **Add an example** button. Add the following example.

    **User:**

    ```code
    New York Baseballers Wins Big Against Chicago
    
    New York Baseballers mounted a big 5-0 shutout against the Chicago Cyclones last night, solidifying their win with a 3 run homerun late in the bottom of the 7th inning.
    
    Pitcher Mario Rogers threw 96 pitches with only two hits for New York, marking his best performance this year.
    
    The Chicago Cyclones' two hits came in the 2nd and the 5th innings, but were unable to get the runner home to score.
    ```

    **Assistant:**

    ```code
    Sports
    ```

1. Add another example with the following text.

    **User:**

    ```code
    Joyous moments at the Oscars

    The Oscars this past week where quite something!
    
    Though a certain scandal might have stolen the show, this year's Academy Awards were full of moments that filled us with joy and even moved us to tears.
    These actors and actresses delivered some truly emotional performances, along with some great laughs, to get us through the winter.
    From Robin Kline's history-making win to a full performance by none other than Casey Jensen herself, don't miss tomorrows rerun of all the festivities.
    ```

    **Assistant:**

    ```code
    Entertainment
    ```

1. Save those changed to the assistant setup, and send the same prompt about California drought, provided here again for convenience.

    ```code
    Severe drought likely in California

    Millions of California residents are bracing for less water and dry lawns as drought threatens to leave a large swath of the region with a growing water shortage.
    
    In a remarkable indication of drought severity, officials in Southern California have declared a first-of-its-kind action limiting outdoor water use to one day a week for nearly 8 million residents.
    
    Much remains to be determined about how daily life will change as people adjust to a drier normal. But officials are warning the situation is dire and could lead to even more severe limits later in the year.
    ```

1. This time the model should respond with an appropriate classification, even without instructions.


## Prompt engineering using code

## Run the application

### .NET CLI:
dotnet run program.cs

### Visual Studio:
To start building the program, press the green Start button on the Visual Studio toolbar, or press F5 or Ctrl+F5. Using the Start button or F5 runs the program under the debugger.

## Clean up

When you're done with your Azure OpenAI resource, remember to delete the deployment or the entire resource in the [Azure portal](https://portal.azure.com?azure-portal=true).
