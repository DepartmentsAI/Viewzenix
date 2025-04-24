import React, { ReactNode, useState } from 'react';
import Sidebar from './Sidebar';
import Navbar from './Navbar';
import styled from 'styled-components';

interface LayoutProps {
  children: ReactNode;
}

const LayoutContainer = styled.div`
  display: flex;
  height: 100vh;
`;

const ContentWrapper = styled.div`
  flex: 1;
  overflow-y: auto;
  background-color: var(--color-surface);
`;

const MainContent = styled.main`
  padding: var(--spacing-lg);
  margin-top: 60px;
  
  @media (max-width: 768px) {
    padding: var(--spacing-md);
  }
`;

const Layout: React.FC<LayoutProps> = ({ children }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  
  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };
  
  return (
    <LayoutContainer>
      <Sidebar isOpen={isSidebarOpen} />
      <ContentWrapper>
        <Navbar toggleSidebar={toggleSidebar} />
        <MainContent>
          {children}
        </MainContent>
      </ContentWrapper>
    </LayoutContainer>
  );
};

export default Layout; 