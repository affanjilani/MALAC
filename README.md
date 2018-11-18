# MALAC Blochacks Submission 
By Artsiom Skliar, Christos Panaritis, Mathieu Vachon, Affan Jilani, Wael Alhashemi

### Description
We used the category IRSS and did the Passport project. How it works is that from an Android app we take a headshot photo to use as that person's passport photo. That .jpg image is transferred to the Node.js server, which in turn sends the image to python scripts that take care of the computer vision component. They make sure that the person was not smiling and if they are frowning or not. In turn, a success or failure message is sent as a response from the server back to the app. If it succeeded, the photographer puts in a digital signature.
