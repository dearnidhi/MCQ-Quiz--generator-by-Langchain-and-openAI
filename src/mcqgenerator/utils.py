import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try: 
            pdf_reader = PyPDF2.PdfFileReader(file)  # corrected assignment operator
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()  # corrected text extraction to accumulate text
            return text  # corrected indentation

        except Exception as e:
            raise Exception("error reading the pdf file")  
    elif file.name.endswith(".txt"):
        return file.read()  # removed decode("utf-8")
    else:
        raise Exception("unsupported file format, only pdf and text files are supported")  # added closing parenthesis

def get_table_data(quiz_str):
    try:
        # Convert the quiz from a str to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(  # corrected variable name to options
                [
                    f"{option}->{option_value}" for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        return quiz_table_data  
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
