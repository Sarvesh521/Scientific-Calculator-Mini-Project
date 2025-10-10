# Scientific Calculator DevOps Mini-Project

This project implements a simple command-line scientific calculator in Python and automates its entire build, test, and deployment lifecycle using a complete CI/CD pipeline. The primary goal is to demonstrate the core principles of DevOps by integrating various tools like Git, Jenkins, Docker, and Ansible.

## Features


The **Scientific Calculator** supports the following mathematical operations:

| Operation | Expression | Description |
|------------|---------------------|--------------|
| **Square Root** |`sqrt(x)` | Computes the square root of a non-negative number. |
| **Factorial** |`fact(x)` | Computes the factorial of an integer (x ≥ 0). |
| **Natural Logarithm** |`ln(x)` | Calculates the natural logarithm (base e). |
| **Power Function** |`pow(x, b)` | Raises x to the power of b. |

## Tech Stack & Tools

| Tool          | Purpose                                        |
| ------------- | ---------------------------------------------- |
| **Git/GitHub**| Source Code Management & CI/CD Trigger         |
| **Python** | Application & Test Scripting Language          |
| **Jenkins** | Continuous Integration/Continuous Deployment Server |
| **Docker** | Application Containerization & Environment Isolation |
| **Docker Hub**| Public Docker Image Registry                   |
| **ngrok** | Exposing Local Jenkins Server to the Internet  |
| **Ansible** | Configuration Management & Automated Deployment |

## DevOps Pipeline Overview

The project is built around a fully automated CI/CD pipeline orchestrated by Jenkins.

1.  **Commit & Push**: A developer pushes code changes to a feature branch on the GitHub repository.
2.  **Webhook Trigger**: GitHub sends a webhook notification to the Jenkins server.
3.  **Jenkins Starts Build**: Jenkins detects the push and automatically starts a new pipeline build for that branch.
4.  **Checkout**: The pipeline checks out the latest source code.
5.  **Test**: Unit tests are run inside a clean Python environment to validate the code.
6.  **Build Docker Image**: If tests pass, Jenkins builds a new Docker image containing the Python application.
7.  **Push to Docker Hub**: The new versioned image is pushed to Docker Hub.
8.  **Deploy with Ansible**: The pipeline executes an Ansible playbook to deploy the new Docker image on the local machine.
9.  **Notify**: A final email notification is sent with the success or failure status of the pipeline.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine (tested on Ubuntu/Debian-based systems):
-   Git
-   Github
-   Docker Engine
-   Python 3 and Pip
-   Ansible
-   [ngrok](https://ngrok.com/download) (for exposing your local Jenkins instance)

## Setup and Installation

Follow these steps to set up the complete environment.

### 1. Clone the Repository
```bash
git clone [https://github.com/Sarvesh521/Scientific-Calculator-Mini-Project.git](https://github.com/Sarvesh521/Scientific-Calculator-Mini-Project.git)
cd Scientific-Calculator-Mini-Project
```

### 2. Set Up Jenkins

1. **Update package list**
   ```bash
   sudo apt update
   ```

2. **Install OpenJDK 17**
   ```bash
   sudo apt install openjdk-17-jdk
   ```

3. **Verify Java installation**
   ```bash
   java --version
   ```

4. **Add Jenkins repository key**
   ```bash
   curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
     /usr/share/keyrings/jenkins-keyring.asc > /dev/null
   ```

5. **Add Jenkins repository**
   ```bash
   echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
     https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
     /etc/apt/sources.list.d/jenkins.list > /dev/null
   ```

6. **Update package list again**
   ```bash
   sudo apt update
   ```

7. **Install Jenkins**
   ```bash
   sudo apt install jenkins
   ```

8. **Enable Jenkins service**
   ```bash
   sudo systemctl enable jenkins
   ```

9. **Start Jenkins service**
   ```bash
   sudo systemctl start jenkins
   ```

10. **Access Jenkins**
    - Open your browser and go to: [http://localhost:8080/](http://localhost:8080/)

11. **Get the initial admin password**
    ```bash
    sudo cat /var/lib/jenkins/secrets/initialAdminPassword
    ```
---

### 3. Configure Jenkins Credentials

#### Docker Hub Credentials

- Navigate: **Manage Jenkins → Credentials → (global) → Add Credentials**
- **Kind:** Username with password  
- **Username:** Your Docker Hub username  
- **Password:** Your Docker Hub password or access token  
- **ID:** `dockerhub-credentials`

#### GitHub Credentials

You need to give Jenkins access to your GitHub repository so it can pull code and trigger builds automatically.

- Navigate: **Manage Jenkins → Credentials → (global) → Add Credentials**
- **Kind:** Personal Access Token (or Username with password, if preferred)
- **Username:** Your GitHub username  
- **Password / Token:** Your GitHub Personal Access Token (PAT)  
  - You can generate one from **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**.
  - Ensure it has at least the following scopes:
    - `repo` — Full control of private repositories  
    - `admin:repo_hook` — Manage webhooks and services  
- **ID:** `github-credentials`
- **Description:** *Access token for GitHub repository integration.*

#### Email Notification Setup

To receive build status notifications (success, failure, etc.) via email, configure the **Email Extension Plugin** in Jenkins.

---

### Step 1: Install the Email Extension Plugin

1. Go to **Manage Jenkins → Plugins → Available plugins**  
2. Search for **Email Extension Plugin**  
3. Check the box and click **Install without restart**

---

### Step 2: Configure SMTP Settings

1. Go to **Manage Jenkins → System**  
2. Scroll down to **Extended E-mail Notification**
3. Fill in your SMTP server details:

   | Field | Example (for Gmail) |
   |--------|--------------------|
   | SMTP server | `smtp.gmail.com` |
   | SMTP Port | `25` |
   | SMTP Username | `your_email@gmail.com` |
   | SMTP Password | *App password (not your Gmail password)* |
   | Default user e-mail suffix | `@gmail.com` |

4. Click **Test configuration** to verify that emails are working.  
   (You’ll receive a test message if it’s set up correctly.)

---

### Step 3: Allow App Passwords (if using Gmail)

If using Gmail, you need to create an **App Password**:

1. Go to **Google Account → Security → App Passwords**
2. Select **App:** Mail → **Device:** Other (Custom name, e.g. “Jenkins”)
3. Copy the 16-character app password.
4. Use this password as your SMTP credential in Jenkins.

---

### Step 4: Configure Email in the Pipeline

Add an **email notification** stage in your `Jenkinsfile`:

```groovy
post {
    success {
        mail to: 'your_email@gmail.com',
             subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
             body: "Good news! The build completed successfully."
    }
    failure {
        mail to: 'your_email@gmail.com',
             subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
             body: "Something went wrong. Please check the Jenkins logs."
    }
}
```
---
### 4. Essential Jenkins Plugins


Most of these are installed automatically if you select **“Install suggested plugins”** during the initial Jenkins setup.

---

#### Plugin List

| Plugin Name | Why It’s Needed |
|--------------|----------------|
| **Pipeline** | This is the **core plugin suite** that allows Jenkins to interpret and execute `Jenkinsfile` scripts. It provides essential features such as `pipeline`, `agent`, `stages`, `steps`, and `post` blocks. Without it, no pipeline will run. |
| **Git** | Enables Jenkins to connect to your GitHub repository using the `checkout scm` step and fetch the project source code. Required for version control integration. |
| **Docker Pipeline** *(docker-workflow)* | Provides all **Docker-related steps** like `docker.build()`, `docker.image().inside()`, and `docker.withRegistry()`. This plugin is essential for building, tagging, and pushing Docker images as part of your CI/CD pipeline. |
| **Credentials** & **Credentials Binding** | These plugins allow you to **securely store and use credentials** (like Docker Hub tokens, GitHub PATs, or sudo passwords) in your pipeline using the `withCredentials` step, without exposing them in logs. |
| **Email Extension** *(email-ext)* | Provides the enhanced `mail` step used in the `post` block to send email notifications on build success or failure. It replaces and improves upon the older “Mailer” plugin. |
| **Pipeline: Multibranch** | Required for the **Multibranch Pipeline** job type. It enables Jenkins to automatically discover, manage, and build branches in your GitHub repository that contain a `Jenkinsfile`. |

---

#### How to Install

1. Go to **Manage Jenkins → Plugins → Available plugins**
2. Search for each of the plugins listed above.
3. Check their boxes and click **Install without restart**
4. Once installation completes, restart Jenkins to activate them.

---

### 5. Create the Jenkins Job

1. From the Jenkins dashboard, click **New Item**.  
2. Enter a name (e.g., `Scientific-Calculator-Pipeline`).  
3. Select **Multibranch Pipeline** → click **OK**.  
4. Under **Branch Sources**, click **Add source** → select **GitHub**.  
5. Enter your repository URL:  
   `https://github.com/Sarvesh521/Scientific-Calculator-Mini-Project.git`  
6. Click **Save**.  
7. Jenkins will automatically scan the repo and find your `Jenkinsfile`.

---

### 6. Expose Jenkins with ngrok

Open a new terminal and start **ngrok** to expose port 8080.

```bash
ngrok http 8080
```

Copy the **HTTPS forwarding URL** provided by ngrok.

---

### 7. Configure GitHub Webhook

1. Go to your GitHub repo → **Settings → Webhooks → Add webhook**.  
2. **Payload URL:** Paste your ngrok URL and add `/github-webhook/` at the end.  
3. **Content type:** `application/json`  
4. **Save the webhook**.  
5. You should see a green checkmark for a successful connection.

---

### 8. Usage: Running the Project


#### Make a Code Change

Edit any file (for example, add a comment in `calculator.py`).

#### Commit and Push

```bash
git add .
git commit -m "My new feature"
git push origin main
```

#### Watch Jenkins Build

Go to your Jenkins dashboard — a new build will start automatically.

#### Interact with the Deployed App

After the pipeline succeeds, the calculator app will run in a Docker container:

```bash
docker attach containerid
```

or 

```bash
docker attach containername
```

---

#### Key Configuration Files

| File | Description |
|------|--------------|
| `Jenkinsfile` | Defines CI/CD pipeline stages from build to deployment. |
| `Dockerfile` | Blueprint for building the calculator app image. |
| `deploy.yml` | Ansible playbook for container deployment. |
| `inventory` | Ansible inventory file (runs deployment on localhost). |
| `calculator.py` | Source code for the calculator application. |
| `test_calculator.py` | Unit tests for the calculator. |

---