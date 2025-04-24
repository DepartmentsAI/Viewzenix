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

export default function Brokers() {
  return (
    <PageContainer>
      <h1>Brokers</h1>
      <p>Configure your broker connections and settings.</p>
      
      <Card>
        <h3>Connected Brokers</h3>
        <p>This section will display your connected broker accounts and their status.</p>
      </Card>
      
      <Card>
        <h3>Connect New Broker</h3>
        <p>This section will allow you to connect to a new broker by providing API keys.</p>
      </Card>
      
      <Card>
        <h3>Broker Settings</h3>
        <p>This section will allow you to configure broker-specific settings and restrictions.</p>
      </Card>
    </PageContainer>
  );
} 