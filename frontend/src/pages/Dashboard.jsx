import Card from "../components/Card";

export default function Dashboard() {
  return (
    <div className="grid grid-cols-3 gap-6 p-6">
      <Card title="Active Users">123</Card>
      <Card title="Tokens Issued">56</Card>
      <Card title="Decoys Deployed">8</Card>
    </div>
  );
}
