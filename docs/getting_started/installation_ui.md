# Installing Moonshot for User Interface

## Preinstallation Requirements

This project <span style="color:red;">strictly</span> requires Python <span style="color:red;">3.11</span>. Ensure that you have Python 3.11 installed on your system before proceeding with installation and usage.

 | Software                                                                           | Version Requirement |
| ---------------------------------------------------------------------------------- | ------------------- |
| [Python](https://www.python.org/downloads/)                                        | v3.11               |
| [NodeJs](https://nodejs.org/en/download)                                           | v20.11.1 LTS or above               |
| npm                                        | v10.8.0 or above               |
| git                                        |                |

It is recommended to create a new Python virtual environment in your working directory before proceeding with installation. To do so, enter working directory and proceed with following steps:

=== "Windows Powershell"

    ``` 
    $ python -m venv venv
    $ venv/Scripts/Activate.ps1
    ```

=== "Windows Command Prompt"

    ```
    $ python -m venv venv
    $ venv/Scripts/activate.bat
    ```

=== "Mac"

    ```
    $ python -m venv venv
    $ source venv/bin/activate
    ```    
  
       
<span style="font-size: 17px">There are 2 ways to install Moonshot - PyPi (Method 1) or Source (Method 2).</span> 

## Method 1: Installation from PyPi 
*You can find the Moonshot Package [here](https://pypi.org/project/projectmoonshot-imda/).* The source code is available on [GitHub](https://github.com/moonshot-admin/moonshot).


### Installing the Moonshot Library
The Moonshot Library allows you to interact with the Moonshot API without any additional features. This is the simplest way to get started with Moonshot if you only need to use the API. Install with:
```
$ pip install aiverify-moonshot
```

### Enabling Moonshot UI
The Moonshot UI enables you to interact with the Moonshot Library through a User Interface. Install with:
```
$ pip install "aiverify-moonshot[web-api]"
```

Alternatively, for the greatest flexibility, to interact with the Moonshot Library through both CLI and HTTP, install with: 
```
$ pip install "aiverify-moonshot[all]"
```

## Method 2: Installation from Source
The source code is available on GitHub [here](https://github.com/moonshot-admin/moonshot). Ensure that [git](https://git-scm.com/downloads) is installed before proceeding with below steps.

1. Download the source files by cloning the repository:
```
$ git clone https://github.com/moonshot-admin/moonshot.git
```
2. Change directory to project's root directory:
```
cd moonshot
```
3. Install the required packages:
```
$ pip install -r requirements.txt
```

## Running Moonshot

1. Before running the Moonshot User Interface, clone Moonshot data and Moonshot UI from GitHub:

    ```
    $ python -m moonshot -i moonshot-data
    $ python -m moonshot -i moonshot-ui
    ```

<span style="font-size: 15px">  Find out more about what `-i moonshot-ui` does [here](../additional_information/additional_information.md).</span>

2. To run the User Interface:

    ```
    $ python -m moonshot web
    ``` 

Access the Web UI from browser `http://localhost:3000`

### Additional Arguments

#### Specify Custom Environment File
If you have a custom '<b>.env</b>' file, specify the path to the file as follows:
```
python -m moonshot -e /path/to/your/.env
```
#### Others

You can also combine additional arguments with Moonshot's run commands like this:

```
python -m moonshot web -i moonshot-data -i moonshot-ui -e /path/to/your/.env
```

This example demonstrates how to launch the Moonshot UI with additional parameters to install <b>moonshot-data</b> and <b>moonshot-ui</b>, and to configure it using a specified '<b>.env</b>' file.