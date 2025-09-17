import Card from "../components/Card";

export default function Tokens() {
  return (
    <div className="page-container">
      <Card title="Token Management">
        <button className="button button-blue">
          Generate Token
        </button>
      </Card>
    </div>
  );
}