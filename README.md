# ExamOS Development Environment

This project uses Docker to create a consistent build environment for ExamOS.

## Prerequisites

- Docker
- Git (or another version control system)

## Final Project Structure

Your project directory must be organized like this for the build to work correctly.

/ExamOS-Project/
├── Dockerfile
└── exam-os-build/
└── config/
├── hooks/
│   └── my-final-setup.chroot
├── includes.chroot/
│   ├── etc/
│   │   └── systemd/
│   │       └── system/
│   │           └── getty@tty1.service.d/
│   │               └── override.conf  <-- Auto-login config
│   ├── home/
│   │   └── examuser/
│   │       ├── .profile         <-- Auto-startx config
│   │       ├── .xinitrc
│   │       └── exam_app.py      <-- Your Python app
│   └── usr/
│       └── share/
│           └── plymouth/
│               └── themes/
│                   └── flame/
└── package-lists/
└── my-system.list.chroot

## Build Instructions

1.  **Build the Builder Image:** From the root of the project, run:
    ```bash
    docker build -t examos-builder .
    ```

2.  **Build the ExamOS.iso:** This command runs the build inside the container and mounts your project directory, so the final `.iso` appears on your local machine.
    ```bash
    docker run --privileged --rm -it -v "$(pwd)/exam-os-build:/app" examos-builder
    ```

3.  **Find Your ISO:** The final `live-image-amd64.iso` will be in your `exam-os-build` directory.
