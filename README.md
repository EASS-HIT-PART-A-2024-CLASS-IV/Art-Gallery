# ArtGallery

Welcome to the ArtGallery repository!
ArtGallery is a dynamic web application designed to showcase a curated collection of artworks. This application is structured into a frontend and backend, encapsulating the user interface and data management logic separately for better maintainability and scalability.

## Quick Start

To get ArtGallery up and running on your machine, ensure you have Docker installed and follow these steps:

### Prerequisites

- Docker
- Docker Compose
- Python 3 (for running tests)
- pytest (for running tests)

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/Adi-Hershko/ArtGallery.git
   cd ArtGallery
   ```


2. **Start the Application with Docker Compose**

   From the root directory of the project, run Docker Compose to start the application. Docker Compose will automatically build (or rebuild) the images as necessary and start all the services defined in the docker-compose.yml file:

   ```bash
   docker-compose up --build -d
   ```

   This command streamlines the process, eliminating the need to manually build each image beforehand.

### Accessing the Application

After starting the services, the ArtGallery application should be accessible through your web browser:

- **Frontend:** http://localhost:5173
- **Backend:** http://localhost:8000

## Testing

To ensure the quality and reliability of the backend service, we employ pytest for running our suite of automated tests. Follow these steps to execute the tests:

1. **Install pytest**
If you haven't already installed `pytest`, you can do so by running:

```bash
pip install pytest
```

2. **Run the Tests**
Navigate to the Backend directory where the `tests` folder is located, and run `pytest`:

```bash
cd Backend
pytest tests
```

`pytest` will automatically discover and run all `tests` in the tests directory, reporting the results in the terminal.

## Features

ArtGallery offers a range of features designed to enhance the experience of exploring and enjoying art:

- **Artwork Showcase:** A curated collection of artworks is displayed in an intuitive and user-friendly interface.
- **Artist Information:** Gain insights into the lives and works of the artists behind the masterpieces.
- **Responsive Design:** The gallery is accessible on any device, thanks to responsive web design principles ensuring a seamless experience across platforms.

Enjoy exploring the ArtGallery!