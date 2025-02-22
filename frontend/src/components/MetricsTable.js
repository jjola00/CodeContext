// frontend/src/components/MetricsTable.js
import React from "react";

const MetricsTable = ({ metrics }) => {
  return (
    <div>
      <h2>Metrics History</h2>
      <table>
        <thead>
          <tr>
            <th>Device</th>
            <th>Metric</th>
            <th>Value</th>
            <th>Unit</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((metric, index) => (
            <tr key={index}>
              <td>{metric.device_name}</td>
              <td>{metric.metric_name}</td>
              <td>{metric.value}</td>
              <td>{metric.unit}</td>
              <td>{new Date(metric.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};


export default MetricsTable;