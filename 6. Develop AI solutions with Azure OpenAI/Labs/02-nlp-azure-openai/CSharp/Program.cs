// Implicit using statements are included
using System.Text;
using System.Text.Json;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Configuration.Json;
using Azure;
// Add Azure OpenAI package
using Azure.AI.OpenAI;

// Build a config object and retrieve user settings.
IConfiguration config = new ConfigurationBuilder()
    .AddJsonFile("appsettings.json")
    .Build();
string? oaiEndpoint = config["AzureOAIEndpoint"];
string? oaiKey = config["AzureOAIKey"];
string? oaiModelName = config["AzureOAIModelName"];

//Set OpenAI configuration settings
OpenAIClient client = new(new Uri(oaiEndpoint), new AzureKeyCredential(oaiKey));
string prompt = "What is the name of the capital of Denmark?";
Console.Write($"Prompt : {prompt}\n");

//Send a completion call to generate an answer
Response<Completions> completionsResponse =
    await client.GetCompletionsAsync(oaiModelName, prompt);
string completion = completionsResponse.Value.Choices[0].Text;
Console.WriteLine($"Azure OpenAI response: {completion}");
