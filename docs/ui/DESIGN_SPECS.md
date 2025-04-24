# Viewzenix UI Design Specifications

This document outlines the design specifications for the Viewzenix user interface.

## Design Principles

1. **Modern & Clean**: Contemporary, minimalist design with ample white space
2. **Responsive**: Fully adaptive across all device sizes (mobile, tablet, desktop)
3. **Accessible**: WCAG 2.1 AA compliant, ensuring accessibility for all users
4. **Consistent**: Unified visual language throughout the application
5. **Intuitive**: User-centric design focused on ease of use

## Color Palette

### Primary Colors
- **Primary**: `#3E63DD` (Blue)
- **Secondary**: `#00BA88` (Green)
- **Accent**: `#8C4BFF` (Purple)

### Neutral Colors
- **Background**: `#FFFFFF` (White)
- **Surface**: `#F8F9FC` (Light Gray)
- **Border**: `#E2E8F0` (Gray)
- **Text - Primary**: `#1A2B4B` (Dark Blue/Gray)
- **Text - Secondary**: `#5A6B8A` (Medium Blue/Gray)
- **Text - Disabled**: `#A0AEBF` (Light Blue/Gray)

### Semantic Colors
- **Success**: `#00BA88` (Green)
- **Warning**: `#F5A623` (Amber)
- **Error**: `#E53E3E` (Red)
- **Info**: `#3E63DD` (Blue)

## Typography

### Font
- **Primary Font**: "Inter", sans-serif

### Text Styles
- **Heading 1**: 32px, Bold, Line Height 40px
- **Heading 2**: 24px, Bold, Line Height 32px
- **Heading 3**: 20px, Bold, Line Height 28px
- **Heading 4**: 18px, Bold, Line Height 24px
- **Body 1**: 16px, Regular, Line Height 24px
- **Body 2**: 14px, Regular, Line Height 20px
- **Caption**: 12px, Regular, Line Height 16px
- **Button Text**: 14px, Medium, Line Height 20px

## Spacing System

Using a 4-point grid system:

- **xs**: 4px
- **sm**: 8px
- **md**: 16px
- **lg**: 24px
- **xl**: 32px
- **2xl**: 48px
- **3xl**: 64px

## UI Components

### Buttons

#### Primary Button
- Background: Primary color
- Text: White
- Hover: Darken primary color by 10%
- Padding: 10px 16px
- Border Radius: 8px

#### Secondary Button
- Background: White
- Text: Primary color
- Border: 1px solid Primary color
- Hover: Light tint of primary color
- Padding: 10px 16px
- Border Radius: 8px

#### Text Button
- Background: Transparent
- Text: Primary color
- Hover: Light tint of primary color
- Padding: 10px 16px

### Form Controls

#### Text Input
- Height: 40px
- Border: 1px solid Border color
- Border Radius: 8px
- Focus: 2px outline of Primary color
- Padding: 8px 12px

#### Dropdown
- Similar styling to Text Input
- With dropdown indicator icon

#### Checkbox & Radio
- Custom styled with brand colors
- Clear focus and selected states

### Cards
- Background: White
- Border: 0
- Border Radius: 12px
- Shadow: 0 4px 6px rgba(0, 0, 0, 0.05)
- Padding: 24px

### Navigation
- Clean, minimal top navigation
- Mobile: Collapsible hamburger menu
- Active state clearly indicated

## Layout Guidelines

### Grid System
- 12-column grid for desktop
- Responsive breakpoints:
  - Mobile: < 768px
  - Tablet: 768px - 1023px
  - Desktop: ≥ 1024px

### Page Structure
- Header: Navigation, user menu
- Main content area
- Footer: Links, copyright

### Content Container
- Max width: 1200px
- Centered on larger screens
- Responsive padding on smaller screens

## Icons

- Consistent icon set using [Material Icons](https://material.io/icons/) or similar
- Regular size: 24px
- Small size: 16px

## Animation & Transitions

- Subtle, purposeful animations
- Standard transition: 150ms ease-in-out
- No excessive or distracting animations

## Responsive Behavior

- Mobile-first approach
- Stacked layouts on mobile
- Side-by-side layouts on larger screens
- Touch-friendly tap targets (min. 44px)

## Image Guidelines

- Product images: 16:9 or 4:3 aspect ratio
- Avatars: 1:1 (square), displayed as circles
- Image optimization for performance

## Accessibility

- Sufficient color contrast (WCAG AA)
- Keyboard navigable interface
- Screen reader compatible
- Focus indicators
- Alternative text for images

*Note: These design specifications will be refined as the project progresses. Detailed component specifications and mockups will be provided during implementation.* 