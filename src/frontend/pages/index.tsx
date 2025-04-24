import React from 'react';
import { useRouter } from 'next/router';
import styled from 'styled-components';
import { useEffect } from 'react';

const PageContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
`;

export default function Home() {
  const router = useRouter();
  
  // Redirect to the webhook setup page
  useEffect(() => {
    router.push('/webhook-setup');
  }, [router]);
  
  return (
    <PageContainer>
      <h2>Redirecting to dashboard...</h2>
    </PageContainer>
  );
} 