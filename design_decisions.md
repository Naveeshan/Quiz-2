# Design Decisions

## Architecture

- **Framework:** Django with Django REST Framework was chosen for fast API building, built-in admin, and authentication support.
- **Database:** Mysql was selected due to compatibility and realistic enterprise use-cases.
- **Data Generation:** Faker library is used to simulate realistic employee and performance data.

## Database Design

Three main models:
- `Employee`: Stores name, position, joining date, department, etc.
- `Departent` : Stores role / name of employees with id.
- `Performance`: Linked to Employee, stores KPIs like efficiency, punctuality.
- `Attendance`: (optional) Logs daily check-in/check-out times.

Relationships:
- One-to-many between Employee -> Department -> Performance and Employee -> Attendance

## REST API Design

- Used DRF's class-based views and `ModelViewSet` for CRUD operations.
- Token-based auth (`rest_framework.authtoken`) for secure access.
- Throttling enabled using `UserRateThrottle`.

## Testing & Validation

- Basic unit tests for model creation and API response.
- Swagger UI for real-time API validation.
- Graceful handling of invalid inputs with DRF error responses.

## Visualizations

- Simple line/bar charts with Chart.js for performance summaries.
- Data is fetched via API and displayed on a minimal HTML template.


## Security

- `.env` used to store sensitive credentials.
- DRF permissions and throttling to prevent abuse.

##  Time Management Strategy

- Phase 1 (0–1 hr): Set up models, data generation script
- Phase 2 (1–2 hr): Create APIs and authentication
- Phase 3 (2–3 hr): Add Swagger, visualization, polish
