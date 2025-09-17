import Card from "../components/Card";

export default function Decoys() {
  return (
    <div className="page-container">
      <Card title="Deploy Decoys">
        <button className="button button-green">
          Deploy New Decoy
        </button>
      </Card>
    </div>
  );
}