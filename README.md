# End-of-Life Bots Infrastructure

**Project Initialization Date:** November 2025

## Description

This software complex (`end-of-life-bots`) is a specialized architectural solution designed for the centralized decommissioning of a pool of Telegram bots.

The system's primary objective is to ensure the correct termination of software product lifecycles, inform end-users about the cessation of support, and maintain an audit trail of any residual activity.

## Functional Capabilities

The system operates in a "stub" mode for a list of tokens provided in the configuration and performs the following functions:

1.  **Automated User Notification (Multilingual):**
    Upon receiving any incoming activity (messages, commands, chat additions), the bot sends a standardized notification (`END_OF_LIFE_MESSAGE`) regarding the permanent termination of service, server shutdown, and data deletion.
    *   **Multilingual Support:** The system automatically detects the user's language code and responds in one of the 27 supported languages (including EN, RU, ES, ZH, PT, DE, AR, and others).

2.  **Advanced Traffic Aggregation & Logging:**
    Despite service termination, the system continues to monitor and log all incoming traffic to a designated administrative channel (`ID_LOGS`).
    *   **Message Logging:** Logs all incoming text messages, keeping the original HTML formatting and entities.
    *   **Service Events:** Tracks technical events such as chat title changes, pinned messages, video chat schedules, payments, giveaways, and user shared events.
    *   **Forwarded Messages:** Detects forwarded messages and logs their origin (user/channel) to a separate audit channel (`ID_FORWARD`).

3.  **Chat Member & Permission Tracking:**
    The system monitors `ChatMemberUpdated` events to track the status of the bot and users within groups and channels.
    *   Logs events: Join, Leave, Kick/Ban, Unban.
    *   **Permission Audit:** detailed logging of changes in administrator or restricted user permissions (e.g., changes in rights to post messages, invite users, manage video chats).

4.  **Media Content Archiving:**
    Incoming media files (photos, documents, voice messages, video notes, animations) are processed and forwarded to a dedicated storage channel (`ID_MEDIA`) for post-analysis or archiving purposes.

5.  **Error Reporting & Monitoring:**
    Built-in error handler captures unhandled exceptions and sends detailed reports (including stack traces and update JSON dumps) to a developer channel (`ID_DEV`).

6.  **Multi-Bot Architecture:**
    A single application instance (`main.py`) handles an unlimited number of tokens simultaneously, optimizing server resources when maintaining a "graveyard" of inactive projects.

## Tech Stack

*   **Language:** Python 3.12+
*   **Framework:** aiogram 3.x
*   **Containerization:** Docker / Docker Compose

## Installation and Startup

1.  Clone the repository.
2.  Create a `.env` file based on the example, defining the following variables:
    *   `TOKENS`: Comma-separated list of bot tokens.
    *   `DEV_TOKEN`: Token for the service bot used for error reporting.
    *   `ID_DEV`: Channel ID for error reports.
    *   `ID_LOGS`: Channel ID for general traffic logs.
    *   `ID_MEDIA`: Channel ID for media archives.
    *   `ID_FORWARD`: Channel ID for tracking forwarded messages.
    *   `LINK_TO_ADMIN`: Contact info for feedback in the shutdown message.
3.  Launch the project using Docker Compose:

```bash
docker-compose up -d --build
```

---
*This project represents the final stage of the supported services' existence and does not imply further feature expansion.*
