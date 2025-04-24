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

export default function Bots() {
  return (
    <PageContainer>
      <h1>Bots</h1>
      <p>Configure your trading bots and automation settings.</p>
      
      <Card>
        <h3>Active Bots</h3>
        <p>This section will display your active trading bots and their status.</p>
      </Card>
      
      <Card>
        <h3>Bot Configuration</h3>
        <p>This section will allow you to configure trading parameters for your bots.</p>
      </Card>
      
      <Card>
        <h3>Global Settings</h3>
        <p>This section will allow you to configure global risk management settings and fail-safes.</p>
      </Card>
    </PageContainer>
  );
} 