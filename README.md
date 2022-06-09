# CodingClinics
## 1. Installing CodingClinics
Please note: CodingClinics is still under development and therefore there are bound to be some problems, especially due to the way the Google API and its authentication works. The goal is to have this resolved by the release of 1.0.0
### 1.1 Supported Platforms
- Linux: Primarily Ubuntu

### 1.2 Installing Dependencies
You will require python3 and pip
<br>To install all required dependencies do the following
```
cd path/to/repo/
python -m pip install --upgrade pip
pip install -r files/requirements.txt
```

### 1.3 Install Program and Files
#### 1.3.1 Installing Using Python Files/Binary Installation
If you are using the binary, skip to 1.3.2

```
cd path/to/repo/
python code_clinic.py install
```

The output will look similiar to this

```
Installing CodeClinics...
Do you want to use the default directory(/usr/local/bin/) [Y/n]: y
    1: Creating Binary...
    2: Created Binary
    3: Making Binary Executable... 
    4: Installing Binary...
    5: Installed Binary
    6: Cleaning up...
```

Rest of installation explained in 1.3.2

#### 1.3.2 Installing Using Binary/File Installation
If you are using the binary file, you should first do the following
```
code_clinic install
```

The output will look similiar to the following example

```
Installing CodeClinics...
    7: Installing Files...
        8: Installing In Default Location(/home/Ubuntu/.codeclinic/)
        9: Installing Log File...
        10: Installed Log File
        11: Installing Settings File...
        12: Installed Settings File
```

#### 1.3.3 Setup
The output should now look something like the following

```
Setting Up...
Please Enter The Calendar ID of the Central Calendar:
```

In CodingClinics we use the Google API and therefore we need to have the calendar ID to determine which calendar
we will be editing to keep all of the CodingClinic bookings and slots in one central location.

<br>You can find the ID of the calendar you want to use as the central calendar by going to the google calendar website and viewing more details of the calendar you wish to use as the central calendar. 

<br>After entering the Calendar ID, the following should be displayed

```
Thank You For Using CodeClinics
Installed CodeClinics
```

If this message is displayed, CodingClinics was installed sucessfully.
