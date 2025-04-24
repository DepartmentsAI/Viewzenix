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

const LogsContainer = styled.div`
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md);
  font-family: monospace;
  height: 300px;
  overflow-y: auto;
`;

const LogEntry = styled.div`
  margin-bottom: var(--spacing-sm);
  padding-bottom: var(--spacing-sm);
  border-bottom: 1px solid var(--color-border);
  font-size: 14px;
  line-height: 1.4;
`;

export default function Logs() {
  return (
    <PageContainer>
      <h1>Logs</h1>
      <p>View system and trading activity logs.</p>
      
      <Card>
        <h3>Trading Activity</h3>
        <LogsContainer>
          <LogEntry>[2023-05-12 14:32:45] Received webhook for BTCUSD. Action: buy, Quantity: 0.05.</LogEntry>
          <LogEntry>[2023-05-12 14:32:46] Processed order for BTCUSD. OrderID: 12345.</LogEntry>
          <LogEntry>[2023-05-12 14:32:47] Successfully placed buy order for BTCUSD at $64340.15.</LogEntry>
          <LogEntry>[2023-05-12 14:40:01] Setting SL order for BTCUSD at $63500.00.</LogEntry>
          <LogEntry>[2023-05-12 14:40:02] Setting TP order for BTCUSD at $65500.00.</LogEntry>
        </LogsContainer>
      </Card>
      
      <Card>
        <h3>System Logs</h3>
        <LogsContainer>
          <LogEntry>[2023-05-12 14:30:00] System started.</LogEntry>
          <LogEntry>[2023-05-12 14:30:02] Connected to Alpaca API.</LogEntry>
          <LogEntry>[2023-05-12 14:30:05] Webhook endpoint active.</LogEntry>
          <LogEntry>[2023-05-12 14:35:00] Cleaning up old orders.</LogEntry>
          <LogEntry>[2023-05-12 14:40:00] Running portfolio health check.</LogEntry>
        </LogsContainer>
      </Card>
    </PageContainer>
  );
} 