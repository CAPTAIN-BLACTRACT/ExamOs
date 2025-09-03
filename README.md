

#  ExamOS Project 🔒

**ExamOS** is a minimal, secure, Debian-based operating system designed from the ground up to provide a locked-down environment for conducting online examinations. It aims to ensure academic integrity by booting directly into a dedicated kiosk application, preventing access to the underlying OS, web browsers, or other distractions.

---

## ✨ Key Features

* **Secure Kiosk Mode:** Boots directly into a fullscreen Python application, bypassing a traditional desktop.
* **Dual-User Roles:**
    * **Student Mode:** An automatic, passwordless login to a restricted `examuser` account.
    * **Admin Mode:** A password-protected `admin` account for managing exams.
* **Minimal Footprint:** Built from a minimal Debian base for fast boot times and low resource usage.
* **Reproducible Builds:** Uses Docker and `live-build` to create a consistent, distributable `.iso` file from this blueprint.

---

## 📂 Final Project Structure

This repository contains the complete blueprint for building the ExamOS `.iso`. Your local project must match this structure.

/ExamOS/
├── Dockerfile
├── README.md
└── exam-os-build/
└── config/
├── hooks/
│   └── my-final-setup.chroot
├── includes.chroot/
│   ├── etc/
│   │   └── systemd/
│   │       └── system/
│   │           └── getty@tty1.service.d/
│   │               └── override.conf
│   ├── home/
│   │   └── examuser/
│   │       ├── .profile
│   │       ├── .xinitrc
│   │       └── exam_app.py
│   └── root/
└── package-lists/
└── my-system.list.chroot


---

## 🏭 Building the Final ISO ("The Factory")

These instructions are for building the final, distributable `live-image-amd64.iso` from the blueprint.

### Step 1: Build the Builder Image
This command creates a Docker image named `examos-builder` that contains all the necessary build tools. You only need to run this once, or when you change the `Dockerfile`.

```bash
docker build -t examos-builder .
Step 2: Build the ExamOS.iso
This command runs the build process inside a container. It will take a long time and download several gigabytes of data.

Bash

docker run --privileged --rm -it -v "$(pwd)/exam-os-build:/app" examos-builder
When finished, the final live-image-amd64.iso will be located in your exam-os-build directory.

🛠️ Recommended Development Workflow ("The Workshop")
You do not need to rebuild the entire ISO for every small code change. Follow this much faster workflow for day-to-day development.

Stage 1: Create a Development VM
Build an initial ExamOS.iso using the instructions above.

Install this ISO to a persistent VirtualBox virtual machine. This is your "Dev VM."

In the Dev VM's settings, create a Shared Folder that links your local source code folder to /home/examuser/shared-code inside the VM.

Stage 2: The Fast Iteration Loop
Edit Code Locally: Make changes to exam_app.py in the shared folder on your main computer.

Test in VM: The changes are instantly available in the Dev VM. Log in as admin to get a desktop, open a terminal, and run python3 /home/examuser/shared-code/exam_app.py to test your changes.

Repeat: Continue editing and testing in minutes without rebuilding the ISO.

Stage 3: Update the Blueprint
Once your new feature is stable, copy the final version of your Python app from the shared folder back into the main project's exam-os-build/config/includes.chroot/home/examuser/ directory.

Commit this change to your Git repository. You are now ready to build a new, final ISO that includes the updated feature.
