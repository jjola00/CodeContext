import React from "react";

function MetricsTable({ metrics }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Timestamp</th>
          <th>CPU Usage (%)</th>
          <th>RAM Usage (%)</th>
        </tr>
      </thead>
      <tbody>
        {metrics.map((m, index) => (
          <tr key={index}>
            <td>{new Date(m.timestamp).toLocaleString()}</td>
            <td>{m.cpu_usage}%</td>
            <td>{m.ram_usage}%</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default MetricsTable;
