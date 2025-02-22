// frontend/src/App.js
import { fetchMetrics } from "./api";
import Dashboard from "./components/Dashboard";
import MetricsTable from "./components/MetricsTable";

const App = () => {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    const loadMetrics = async () => {
      const data = await fetchMetrics();
      setMetrics(data);
    };
    loadMetrics();
  }, []);

  return (
    <div>
      <h1>System Monitor</h1>
      <Dashboard metrics={metrics} />
      <MetricsTable metrics={metrics} />
    </div>
  );
};

export default App;