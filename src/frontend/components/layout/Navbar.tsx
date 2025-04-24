import React from 'react';
import styled from 'styled-components';
import { FaBars, FaBell, FaUser } from 'react-icons/fa';

interface NavbarProps {
  toggleSidebar: () => void;
}

const NavbarContainer = styled.nav`
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--spacing-lg);
  height: 60px;
  background-color: var(--color-background);
  border-bottom: 1px solid var(--color-border);
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  z-index: 10;
`;

const LeftSection = styled.div`
  display: flex;
  align-items: center;
`;

const MenuButton = styled.button`
  background: none;
  color: var(--color-text-primary);
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: var(--spacing-md);
  
  &:hover {
    color: var(--color-primary);
  }
`;

const RightSection = styled.div`
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
`;

const IconButton = styled.button`
  background: none;
  color: var(--color-text-primary);
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  
  &:hover {
    color: var(--color-primary);
  }
`;

const NotificationDot = styled.span`
  position: absolute;
  top: -2px;
  right: -2px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--color-error);
`;

const UserAvatar = styled.div`
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: var(--color-surface);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-primary);
  font-size: 14px;
  margin-left: var(--spacing-md);
  border: 1px solid var(--color-border);
`;

const Navbar: React.FC<NavbarProps> = ({ toggleSidebar }) => {
  return (
    <NavbarContainer>
      <LeftSection>
        <MenuButton onClick={toggleSidebar}>
          <FaBars />
        </MenuButton>
        <h4>Viewzenix Dashboard</h4>
      </LeftSection>
      <RightSection>
        <IconButton>
          <FaBell />
          <NotificationDot />
        </IconButton>
        <UserAvatar>
          <FaUser />
        </UserAvatar>
      </RightSection>
    </NavbarContainer>
  );
};

export default Navbar; 