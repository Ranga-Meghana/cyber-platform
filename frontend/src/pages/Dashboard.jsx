import Card from "../components/Card";

export default function Dashboard() {
  return (
    <div className="dashboard-grid">
      <Card title="Active Users">123</Card>
      <Card title="Tokens Issued">56</Card>
      <Card title="Decoys Deployed">8</Card>
    </div>
  );
}