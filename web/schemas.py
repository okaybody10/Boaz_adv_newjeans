from fastapi import Form, File, UploadFile
from pydantic import BaseModel


# https://stackoverflow.com/a/60670614
class AwesomeForm(BaseModel):
    text_input: str
    image_upload: UploadFile

    @classmethod
    def as_form(
        cls,
        text_input: str = Form(...),
        image_upload: UploadFile = File(...)
    ):
        return cls(
            text_input=text_input,
            image_upload=image_upload
        )