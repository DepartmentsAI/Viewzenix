import React from 'react';
import styled from 'styled-components';

const PageContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
`;

const Card = styled.div`
  background-color: var(--color-background);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  padding: var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
`;

const WebhookUrl = styled.div`
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md);
  font-family: monospace;
  margin: var(--spacing-md) 0;
  position: relative;
`;

const CopyButton = styled.button`
  position: absolute;
  top: var(--spacing-sm);
  right: var(--spacing-sm);
  background-color: var(--color-primary);
  color: white;
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--border-radius-sm);
  font-size: 12px;
  
  &:hover {
    background-color: var(--color-info);
  }
`;

const JsonExample = styled.pre`
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md);
  font-family: monospace;
  margin: var(--spacing-md) 0;
  overflow-x: auto;
`;

export default function WebhookSetup() {
  return (
    <PageContainer>
      <h1>Webhook Setup</h1>
      <p>Configure your TradingView alerts to send signals to your Viewzenix webhook endpoint.</p>
      
      <Card>
        <h3>Your Webhook URL</h3>
        <p>Use this URL in your TradingView alert settings:</p>
        <WebhookUrl>
          https://api.viewzenix.com/webhook/tv/your-api-key
          <CopyButton>Copy</CopyButton>
        </WebhookUrl>
      </Card>
      
      <Card>
        <h3>TradingView Alert Format</h3>
        <p>Use the following JSON format in your TradingView alert message:</p>
        <JsonExample>{`{
  "symbol": "BTCUSD",
  "strategy_order_id": "long",
  "strategy_order_action": "buy",
  "strategy_order_contracts": 0.05,
  "strategy_order_price": 64340.15,
  "strategy_order_comment": "Breakout",
  "time": 1713746400000
}`}</JsonExample>
      </Card>
      
      <Card>
        <h3>TradingView Alert Generator</h3>
        <p>Coming soon: A visual tool to help you generate the correct alert format for your strategy.</p>
      </Card>
    </PageContainer>
  );
} 