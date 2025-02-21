// frontend/src/components/Controls.js
import React from "react";

const Controls = ({ onAction }) => {
  const actions = ["restart", "shutdown", "update"];

  return (
    <div>
      <h2>Remote Actions</h2>
      {actions.map((action) => (
        <button key={action} onClick={() => onAction(action)}>
          {action}
        </button>
      ))}
    </div>
  );
};

export default Controls;