# GPT4-Vision_GradioApp
# Image Analysis with GPT-4 Vision Preview

This Python code allows you to extract useful details from a document image, such as the type of document, document number, name of the person, nationality, and date of birth. The code uses the GPT-4 Vision Preview API to analyze the image and extract the relevant information as JSON key value pair that can be used by downstream applications.

## Installation

To use this code, you will need to install the following Python packages:

- `base64`
- `requests`
- `gradio`
- `tempfile`
- `Pillow`
- `uuid`

You can install these packages using `pip`. For example:

```
pip install requests
```

You can directly install all dependencies by running the `requirements.txt` file
```
pip install -r requirements. txt
```

## Usage

To use this code, you will need to obtain an API key for the GPT-4 Vision Preview API. You can then set the `api_key` variable in the code to your API key.
Once you have set your API key, you can run the code and provide an image to analyze. The code will extract the relevant information from the image and return it as a JSON object with the following keys:

- `document_type`
- `document_number`
- `name`
- `nationality`
- `date_of_birth`

If the code is unable to identify any of these details, the corresponding key will be blank.

The code leverages Gradio framework to create a simple UI to upload image and retrieve a JSON output

## UI rendered by Gradio
<img width="1249" alt="image" src="https://github.com/DefiMan1729/GPT4-Vision_AppUI/assets/115624087/5f5c3bd7-2517-443c-9b89-14cd0dcba0b0">

This will output a JSON object with the relevant details extracted from the image.

This Python code creates a Gradio interface for the `create_upload_file` function. The interface allows the user to upload an image and then analyzes the image to extract relevant information. The extracted information is then displayed as text.

The `gr.Interface` function is used to create the interface. The `fn` parameter specifies the function to be wrapped by the interface, which in this case is `create_upload_file`. The `inputs` parameter specifies the input component of the interface, which is an image upload component. The `outputs` parameter specifies the output component of the interface, which is a text component.

Once the interface has been created, the `launch` method is called to start the interface. This will open a web page in the default browser, where the user can upload an image and view the extracted information.

## Business Case
The extracted information can be converted into an editable and searchable format. For instance you can now design UIs that are intelligent enough to guide users to upload the right documents required by the application or prevent the user from uploading incorrect documents for a business process, thus enabling straight through processes. It can verify basic details from the uploaded document (image) and empower downstream systems. 
