# MigrateX: Enterprise Service Management Platform

MigrateX is a comprehensive enterprise service management platform that provides integrated data, cloud, IoT, and security services through a unified dashboard interface. The platform offers real-time monitoring, alerting capabilities, and comprehensive management tools across six core modules.

## 🚀 Features

### Core Modules
1. **Data Services**
   - Data Governance
   - Data Quality Management
   - Master Data Management
   - Real-time Data Metrics

2. **Cloud Management**
   - Migration Services
   - Resource Monitoring
   - Cost Optimization
   - Performance Tracking

3. **IoT Operations**
   - Device Management
   - Platform Services
   - Real-time Analytics
   - Gateway Monitoring

4. **Security Services**
   - Threat Detection
   - Incident Response
   - Compliance Monitoring
   - Security Metrics

5. **Cost Management**
   - Cost Tracking
   - Budget Optimization
   - Resource Allocation
   - Savings Recommendations

6. **Compliance Management**
   - Policy Monitoring
   - Compliance Reporting
   - Audit Management
   - Violation Tracking

### Key Features
- Real-time Monitoring Dashboard
- Centralized Alert Management
- Resource Performance Tracking
- Cost Optimization Tools
- Compliance Monitoring
- Interactive Data Visualization

## 📋 Requirements

- Python 3.11+
- PostgreSQL Database
- Streamlit
- Plotly
- Pandas
- psycopg2-binary

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/VictorOladosu/MigrateX.git
cd MigrateX
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
DATABASE_URL=postgresql://user:password@host:port/dbname
PGUSER=your_db_user
PGPASSWORD=your_db_password
PGHOST=your_db_host
PGPORT=your_db_port
PGDATABASE=your_db_name
```

## 🚀 Quick Start

1. Initialize the database:
```bash
python -c "from database import init_db; init_db()"
```

2. Run the application:
```bash
streamlit run main.py
```

## 🏗️ Architecture

The platform is built with a modular architecture:

- `main.py`: Application entry point and main dashboard
- `database.py`: Database connection and initialization
- `models.py`: Data models and database operations
- `components/`: Reusable UI components and utilities
  - `monitoring.py`: Real-time monitoring system
  - `alerts.py`: Alert management system
  - `metrics.py`: Metric collection and display
  - `charts.py`: Data visualization components
- `pages/`: Individual module pages
  - Data Services
  - Cloud Management
  - IoT Operations
  - Security Services
  - Cost Management
  - Compliance Management

## 📊 Features In Detail

### Real-time Monitoring
- Service health monitoring
- Resource utilization tracking
- Performance metrics
- Custom alert thresholds

### Alert Management
- Real-time alert generation
- Customizable thresholds
- Alert history tracking
- Priority-based notifications

### Metric Collection
- CPU and memory usage
- Response time monitoring
- Error rate tracking
- Custom metric support

## 🔧 Configuration

### Database Configuration
The application uses PostgreSQL for data storage. Configure your database connection in the environment variables.

### Monitoring Configuration
Adjust alert thresholds in `components/monitoring.py`:
```python
alert_thresholds = {
    'cpu_usage': 80.0,
    'memory_usage': 85.0,
    'response_time': 800.0,
    'error_rate': 2.0
}
```

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

For support, email support@migratex.com or open an issue in the GitHub repository.
