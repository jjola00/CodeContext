// frontend/src/components/MetricsTable.js
import React from "react";

const MetricsTable = ({ metrics }) => {
  return (
    <div>
      <h2>Metrics History</h2>
      <table>
        <thead>
          <tr>
            <th>Device ID</th>
            <th>CPU Usage</th>
            <th>Memory Usage</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((metric, index) => (
            <tr key={index}>
              <td>{metric.device_id}</td>
              <td>{metric.cpu_usage}%</td>
              <td>{metric.memory_usage}%</td>
              <td>{metric.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MetricsTable;