import * as React from 'react';
import Config from 'route/config/Config';
import { cleanup, render, screen, waitFor } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';

const mockNavigate = jest.fn();
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => mockNavigate,
}));

Object.defineProperty(AbortSignal, 'timeout', {
  value: jest.fn(),
  writable: false,
});

const initialEnv = { ...window.env };

describe('Config', () => {
  const mockResponse = {
    ok: true,
    status: 200,
    json: async () => ({ data: 'success' }),
  };
  beforeEach(() => {
    window.env = { ...initialEnv };
    global.fetch = jest.fn().mockResolvedValue(mockResponse);
  });

  afterEach(() => {
    cleanup();
    jest.resetAllMocks();
  });

  test('renders DeveloperConfig correctly', async () => {
    render(
      <MemoryRouter>
        <Config role="developer" />
      </MemoryRouter>,
    );

    expect(screen.getByText(/Verifying configuration/i)).toBeInTheDocument();
    expect(screen.getByTestId('loading-icon')).toBeInTheDocument();
    await waitFor(() => {
      expect(screen.getByText(/Config verification/i)).toBeInTheDocument();
    });
    expect(screen.getByText(/REACT_APP_URL_BASENAME/i)).toBeInTheDocument();
    expect(
      screen.getByText(/REACT_APP_WORKBENCHLINK_JUPYTERLAB/i),
    ).toBeInTheDocument();
    expect(
      screen.getByText(/REACT_APP_LOGOUT_REDIRECT_URI/i),
    ).toBeInTheDocument();
  });

  test('renders invalid UserConfig correctly', async () => {
    // Invalidate one config field to show user config
    window.env.REACT_APP_GITLAB_SCOPES = 'invalid';
    render(
      <MemoryRouter>
        <Config role="user" />
      </MemoryRouter>,
    );

    expect(screen.getByText(/Verifying configuration/i)).toBeInTheDocument();
    expect(screen.getByTestId('loading-icon')).toBeInTheDocument();
    await waitFor(() => {
      expect(
        screen.getByText(/Invalid Application Configuration/i),
      ).toBeInTheDocument();
    });
    const linkToDeveloperConfig = screen.getByRole('link', {
      name: /Inspect configuration/i,
    });
    expect(linkToDeveloperConfig).toBeInTheDocument();
    expect(linkToDeveloperConfig).toHaveAttribute('href', './developer');
  });

  test('renders valid UserConfig correctly', async () => {
    render(
      <MemoryRouter>
        <Config role="user" />
      </MemoryRouter>,
    );

    expect(screen.getByText(/Verifying configuration/i)).toBeInTheDocument();
    expect(screen.getByTestId('loading-icon')).toBeInTheDocument();
    await waitFor(() => {
      expect(
        screen.getByText(/Configuration appears to be valid./i),
      ).toBeInTheDocument();
    });
    const linkToDeveloperConfig = screen.getByRole('link', {
      name: /Return to login/i,
    });
    expect(linkToDeveloperConfig).toBeInTheDocument();
    expect(linkToDeveloperConfig).toHaveAttribute('href', '/');
  });
});
