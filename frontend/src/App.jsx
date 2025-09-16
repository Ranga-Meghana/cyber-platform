import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";
import Users from "./pages/Users";
import Tokens from "./pages/Tokens";
import Decoys from "./pages/Decoys";
import Replay from "./pages/Replay";
import Attribution from "./pages/Attribution";

export default function App() {
  return (
    <Router>
      <div className="flex">
        <Sidebar />
        <div className="flex-1">
          <Navbar />
          <Routes>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/users" element={<Users />} />
            <Route path="/tokens" element={<Tokens />} />
            <Route path="/decoys" element={<Decoys />} />
            <Route path="/replay" element={<Replay />} />
            <Route path="/attribution" element={<Attribution />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}
