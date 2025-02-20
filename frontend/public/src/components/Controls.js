import React from "react";

function Controls() {
  const sendAction = (action) => {
    fetch(`/${action}`, { method: "POST" }).then((res) =>
      alert(`${action} command sent`)
    );
  };

  return (
    <div>
      <h2>Remote Actions</h2>
      <button onClick={() => sendAction("restart")}>Restart</button>
      <button onClick={() => sendAction("shutdown")}>Shutdown</button>
    </div>
  );
}

export default Controls;
