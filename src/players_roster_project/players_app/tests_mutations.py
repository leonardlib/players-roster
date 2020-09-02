from graphene.test import Client
from .models import Team, Player
from ..schema import schema
from django.test.testcases import TestCase
from mixer.backend.django import mixer


class PlayersMutationsTests(TestCase):
    def setUp(self):
        """
        Prepare GraphQL schema for tests
        :author: @leonard_lib
        :date: 2020-09-302
        :return:
        """
        super().setUp()
        self.client = Client(schema)

    def test_create_team_mutation(self):
        """
        Test API call for create team mutation
        :author: @leonard_lib
        :date: 2020-09-302
        :return:
        """
        query = '''
            mutation createTeamMutation(
                $input: CreateOrUpdateTeamMutationInput!
            ) {
                createOrUpdateTeam(input: $input) {
                    team {
                        id
                        name
                    }
                }
            }
        '''
        input = {
            'name': 'San Antonio Spurs'
        }

        response = self.client.execute(query, variables={
            'input': input
        })
        self.assertIsNotNone(response, 'RESPONSE IS NONE')
        data = response['data']

        team = data['createOrUpdateTeam']['team']
        self.assertIsNotNone(team, 'TEAM IS NONE')
        self.assertEqual(input['name'], team['name'])

    def test_update_team_mutation(self):
        """
        Test API call for update team mutation
        :author: @leonard_lib
        :date: 2020-09-302
        :return:
        """
        query = '''
            mutation updateTeamMutation(
                $input: CreateOrUpdateTeamMutationInput!
            ) {
                createOrUpdateTeam(input: $input) {
                    team {
                        id
                        name
                    }
                }
            }
        '''
        aux_team = mixer.blend(Team)
        input = {
            'id': aux_team.id,
            'name': 'San Antonio Spurs'
        }

        response = self.client.execute(query, variables={
            'input': input
        })
        self.assertIsNotNone(response, 'RESPONSE IS NONE')
        data = response['data']

        team = data['createOrUpdateTeam']['team']
        self.assertIsNotNone(team, 'TEAM IS NONE')
        self.assertEqual(input['id'], int(team['id']))
        self.assertEqual(input['name'], team['name'])

    def test_create_player_mutation(self):
        """
        Test API call for create player mutation
        :author: @leonard_lib
        :date: 2020-09-302
        :return:
        """
        query = '''
            mutation createPlayerMutation(
                $input: CreateOrUpdatePlayerMutationInput!
            ) {
                createOrUpdatePlayer(input: $input) {
                    player {
                        id
                        firstName
                        lastName
                        fullName
                        jerseyNumber
                        team {
                            id
                            name
                        }
                    }
                }
            }
        '''
        team = mixer.blend(Team)
        input = {
            'firstName': 'Michael',
            'lastName': 'Jordan',
            'jerseyNumber': 23,
            'team': team.id
        }

        response = self.client.execute(query, variables={
            'input': input
        })
        self.assertIsNotNone(response, 'RESPONSE IS NONE')
        data = response['data']

        player = data['createOrUpdatePlayer']['player']
        self.assertIsNotNone(player, 'PLAYER IS NONE')
        self.assertEqual(input['firstName'], player['firstName'])
        self.assertEqual(input['lastName'], player['lastName'])
        self.assertEqual(input['jerseyNumber'], player['jerseyNumber'])
        self.assertEqual(input['team'], int(player['team']['id']), 'TEAM IS NOT EQUAL')

    def test_update_player_mutation(self):
        """
        Test API call for update player mutation
        :author: @leonard_lib
        :date: 2020-09-302
        :return:
        """
        query = '''
            mutation updatePlayerMutation(
                $input: CreateOrUpdatePlayerMutationInput!
            ) {
                createOrUpdatePlayer(input: $input) {
                    player {
                        id
                        firstName
                        lastName
                        fullName
                        jerseyNumber
                        team {
                            id
                            name
                        }
                    }
                }
            }
        '''
        team = mixer.blend(Team)
        aux_player = mixer.blend(Player, team=team)
        input = {
            'id': aux_player.id,
            'firstName': 'Kobe',
            'lastName': 'Bryant',
            'jerseyNumber': 24,
            'team': team.id
        }

        response = self.client.execute(query, variables={
            'input': input
        })
        self.assertIsNotNone(response, 'RESPONSE IS NONE')
        data = response['data']

        player = data['createOrUpdatePlayer']['player']
        self.assertIsNotNone(player, 'PLAYER IS NONE')
        self.assertEqual(input['id'], int(player['id']))
        self.assertEqual(input['firstName'], player['firstName'])
        self.assertEqual(input['lastName'], player['lastName'])
        self.assertEqual(input['jerseyNumber'], player['jerseyNumber'])
        self.assertEqual(input['team'], int(player['team']['id']), 'TEAM IS NOT EQUAL')
