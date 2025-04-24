import React from 'react';
import styled from 'styled-components';
import Link from 'next/link';
import { FaLink, FaChartLine, FaExchangeAlt, FaRobot, FaFileAlt } from 'react-icons/fa';

interface SidebarProps {
  isOpen: boolean;
}

const SidebarContainer = styled.aside<{ isOpen: boolean }>`
  width: ${({ isOpen }) => (isOpen ? '240px' : '60px')};
  height: 100vh;
  background-color: var(--color-background);
  border-right: 1px solid var(--color-border);
  transition: width 0.3s ease;
  overflow-x: hidden;
  position: relative;
  z-index: 5;
`;

const Logo = styled.div`
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid var(--color-border);
  padding: var(--spacing-md);
  font-weight: bold;
  color: var(--color-primary);
  font-size: 20px;
`;

const Nav = styled.nav`
  padding: var(--spacing-md) 0;
`;

const NavItem = styled.div<{ active?: boolean }>`
  display: flex;
  align-items: center;
  padding: var(--spacing-sm) var(--spacing-md);
  color: ${({ active }) => (active ? 'var(--color-primary)' : 'var(--color-text-primary)')};
  font-weight: ${({ active }) => (active ? 'bold' : 'normal')};
  border-left: ${({ active }) => (active ? '3px solid var(--color-primary)' : '3px solid transparent')};
  margin-bottom: var(--spacing-xs);
  transition: all 0.2s ease;
  
  &:hover {
    background-color: var(--color-surface);
    color: var(--color-primary);
  }
`;

const IconWrapper = styled.div`
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: var(--spacing-md);
`;

const LinkText = styled.span<{ isOpen: boolean }>`
  opacity: ${({ isOpen }) => (isOpen ? '1' : '0')};
  transition: opacity 0.3s ease;
  white-space: nowrap;
`;

const navigationItems = [
  { name: 'Webhook Setup', icon: <FaLink />, path: '/webhook-setup' },
  { name: 'Brokers', icon: <FaExchangeAlt />, path: '/brokers' },
  { name: 'Bots', icon: <FaRobot />, path: '/bots' },
  { name: 'Logs', icon: <FaFileAlt />, path: '/logs' },
  { name: 'Analytics', icon: <FaChartLine />, path: '/analytics' },
];

const Sidebar: React.FC<SidebarProps> = ({ isOpen }) => {
  return (
    <SidebarContainer isOpen={isOpen}>
      <Logo>V</Logo>
      <Nav>
        {navigationItems.map((item) => (
          <Link href={item.path} key={item.path}>
            <NavItem>
              <IconWrapper>{item.icon}</IconWrapper>
              <LinkText isOpen={isOpen}>{item.name}</LinkText>
            </NavItem>
          </Link>
        ))}
      </Nav>
    </SidebarContainer>
  );
};

export default Sidebar; 