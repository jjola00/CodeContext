// frontend/src/components/Dashboard.js
const Dashboard = ({ metrics }) => {
  return (
    <div>
      <h2>Live Metrics</h2>
      <pre>{JSON.stringify(metrics, null, 2)}</pre>
    </div>
  );
};

export default Dashboard;