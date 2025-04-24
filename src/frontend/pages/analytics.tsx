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

const GridLayout = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
`;

const Stat = styled.div`
  text-align: center;
  padding: var(--spacing-md);
  background-color: var(--color-surface);
  border-radius: var(--border-radius-md);
`;

const StatValue = styled.div`
  font-size: 28px;
  font-weight: bold;
  color: var(--color-primary);
  margin-bottom: var(--spacing-xs);
`;

const StatLabel = styled.div`
  font-size: 14px;
  color: var(--color-text-secondary);
`;

const ChartPlaceholder = styled.div`
  height: 300px;
  background-color: var(--color-surface);
  border: 1px dashed var(--color-border);
  border-radius: var(--border-radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-secondary);
`;

export default function Analytics() {
  return (
    <PageContainer>
      <h1>Analytics</h1>
      <p>View performance metrics and trading statistics.</p>
      
      <GridLayout>
        <Stat>
          <StatValue>12</StatValue>
          <StatLabel>Total Trades</StatLabel>
        </Stat>
        <Stat>
          <StatValue>67%</StatValue>
          <StatLabel>Win Rate</StatLabel>
        </Stat>
        <Stat>
          <StatValue>$1,245</StatValue>
          <StatLabel>Profit/Loss</StatLabel>
        </Stat>
        <Stat>
          <StatValue>1.8</StatValue>
          <StatLabel>Profit Factor</StatLabel>
        </Stat>
      </GridLayout>
      
      <Card>
        <h3>Performance Chart</h3>
        <ChartPlaceholder>Chart visualization will be displayed here</ChartPlaceholder>
      </Card>
      
      <Card>
        <h3>Trade Distribution</h3>
        <ChartPlaceholder>Trade distribution chart will be displayed here</ChartPlaceholder>
      </Card>
    </PageContainer>
  );
} 